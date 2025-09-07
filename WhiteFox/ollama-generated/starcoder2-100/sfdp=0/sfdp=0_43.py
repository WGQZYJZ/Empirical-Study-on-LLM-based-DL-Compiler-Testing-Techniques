
class TransformerModel(torch.nn.Module):
    def __init__(self, embedding_dim, vocab_size):
        super().__init__()
 
        self.embedding  = torch.nn.Embedding(vocab_size, embedding_dim)
        
        self.tokenized_input1 = torch.randint(0, 57829, (32,))
        self.tokenized_input2 = torch.randint(0, 57829, (32,))
 
        embedding1 = self.embedding(self.tokenized_input1)
        embedding2 = self.embedding(self.tokenized_input2)
        
        self.scaled_dot_product  = torch.matmul(embedding1, embedding2.transpose(-2, -1)) / math.sqrt(embedding_dim)
        attention_weights  = self.scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(embedding1)

    def forward(self):
        return self.output


# Initializing the model