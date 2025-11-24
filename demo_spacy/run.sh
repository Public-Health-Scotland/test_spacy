# Measure execution time for spaCy training
echo "Starting spaCy training..."
start=$(date +%s)

python -m spacy train demo_spacy/config.cfg \
    --output .model/ner_dose_model \
    --paths.train data/train.spacy \
    --paths.dev data/dev.spacy

end=$(date +%s)
runtime=$((end - start))

echo "Training completed in $runtime seconds."
