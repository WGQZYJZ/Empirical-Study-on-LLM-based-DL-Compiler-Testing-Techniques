
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key = torch.nn.Linear(16, 32)
 
    def forward(self, query, key, attn_mask):
        vq = self.query @ self.key.transpose(-2, -1) / math.sqrt(self.key.weight.shape[-1])  # Compute the dot product of the query and key, and scale it
        vq += attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(vq, dim=-1)  # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
        return attn_weight @ self.value
 
    def load_weights(self, file):
        self.__dict__.update(torch.load(file))
 
class BertForSequenceClassification(nn.Module):
    # Load pretrained model for classification of MNLI
    def __init__(self, bert, num_labels=2):
        super().__init__()
        # Initialize the Transformer
        self.bert = bert
        
        # Classifier layer to output probabilities of class 1 and class 0
        self.classifier = nn.Linear(768, num_labels)
    
    def forward(self, input_ids=None, attention_mask=None, token_type_ids=None):
        seq_features = self.bert(
            input_ids=input_ids, 
            attention_mask=attention_mask,
            token_type_ids=token_type_ids)[0]

        # Pass BERT output through a linear layer to get probabilities
        sequence_output = self.classifier(seq_features)
        
        return sequence_output
 
# Initializing the model with pretrained weights
model = BertForSequenceClassification()
bert, vocab = torch_hub.load('huggingface/transformers', 'bert-base-cased', force_download=True)
model.bert = bert # Replace pretrained Transformer with a new one 
tokenizer = BertTokenizerFast.from_pretrained(vocab)


# Generate input text (must match the model requirements)
input_ids, segment_ids, attention_mask = generate_sequence_for_bert_classification(model, tokenizer, ["How do you do today?"]) # "how" is missing here


