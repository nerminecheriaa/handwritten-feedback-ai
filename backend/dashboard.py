import streamlit as st
from pathlib import Path
import tempfile

from pipeline import StudentExpectationPipeline


# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Student Expectations AI",
    page_icon="🎓",
    layout="wide"
)


# ============================================================
# TITLE
# ============================================================

st.title("🎓 Student Expectations AI")

st.markdown(
    """
    ### Analyse intelligente des attentes des étudiants

    Importez une feuille manuscrite pour obtenir automatiquement :
    
    - 📝 sa transcription
    - 🎯 les attentes détectées
    - 🟢 les attentes positives
    - 🔴 les attentes négatives
    - 📚 leur catégorie
    """
)


st.divider()


# ============================================================
# UPLOAD
# ============================================================

uploaded_file = st.file_uploader(
    "📤 Importez une feuille manuscrite",
    type=["jpg", "jpeg", "png"],
    help="Formats acceptés : JPG, JPEG et PNG"
)


# ============================================================
# PROCESS
# ============================================================

if uploaded_file is not None:

    st.subheader("📄 Feuille sélectionnée")

    col1, col2 = st.columns(2)

    with col1:

        st.image(
            uploaded_file,
            caption="Document importé",
            use_container_width=True
        )

    with col2:

        st.info(
            f"Fichier : {uploaded_file.name}"
        )

        st.write(
            f"Taille : {uploaded_file.size / 1024:.1f} KB"
        )


    if st.button(
        "🚀 Analyser la feuille",
        type="primary",
        use_container_width=True
    ):

        try:

            # ------------------------------------------------
            # Save uploaded image temporarily
            # ------------------------------------------------

            suffix = Path(
                uploaded_file.name
            ).suffix

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=suffix
            ) as temp_file:

                temp_file.write(
                    uploaded_file.getbuffer()
                )

                temp_image_path = temp_file.name


            # ------------------------------------------------
            # Run pipeline
            # ------------------------------------------------

            pipeline = StudentExpectationPipeline()

            with st.spinner(
                "🤖 Analyse de la feuille en cours..."
            ):

                result = pipeline.process(
                    temp_image_path
                )


            # ------------------------------------------------
            # TRANSCRIPTION
            # ------------------------------------------------

            st.divider()

            st.subheader("📝 Transcription")

            st.text_area(
                "Texte extrait",
                value=result["transcription"],
                height=200
            )


            # ------------------------------------------------
            # EXPECTATIONS
            # ------------------------------------------------

            st.subheader(
                "🎯 Attentes détectées"
            )

            expectations = result[
                "expectations"
            ]


            if not expectations:

                st.warning(
                    "Aucune attente détectée."
                )

            else:

                positive_count = 0
                negative_count = 0


                for expectation in expectations:

                    sentiment = (
                        expectation.sentiment
                    )

                    category = (
                        expectation.category
                    )

                    text = (
                        expectation.text
                    )


                    # ----------------------------------------
                    # POSITIVE
                    # ----------------------------------------

                    if sentiment == "positive":

                        positive_count += 1

                        st.success(
                            f"🟢 POSITIVE — {category}\n\n"
                            f"{text}"
                        )


                    # ----------------------------------------
                    # NEGATIVE
                    # ----------------------------------------

                    else:

                        negative_count += 1

                        st.error(
                            f"🔴 NEGATIVE — {category}\n\n"
                            f"{text}"
                        )


                # ------------------------------------------------
                # SUMMARY
                # ------------------------------------------------

                st.divider()

                st.subheader(
                    "📊 Résumé"
                )

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.metric(
                        "Total",
                        len(expectations)
                    )

                with col2:

                    st.metric(
                        "🟢 Positives",
                        positive_count
                    )

                with col3:

                    st.metric(
                        "🔴 Négatives",
                        negative_count
                    )


        except Exception as e:

            st.error(
                "❌ Une erreur est survenue pendant "
                "l'analyse."
            )

            st.exception(e)