
class Model(torch.nn.Module):
    def __init__(self, key_size=8, hidden_size=32, num_head=8):
        super().__init__()
        self.layer = torch.nn.TransformerEncoderLayer(
            self.key_size, 
            self.hidden_size, 
            self.num_head, 
            self.scale, 
            self.dropout)

    def forward(self, x1, x2):
        q1 = self.layer.query(x1).transpose(-2, -1)  # Compute the query vector from (batch size, input length, embedding dim) to (batch size, input length, key dim)
        k1 = self.layer.key(x1).transpose(-2, -1)  # Compute the key vector from (batch size, input length, embedding dim) to (batch size, input length, key dim)
        v1 = self.layer.value(x1).transpose(-2, -1)  # Compute the value vector from (batch size, input length, embedding dim) to (batch size, input length, value dim)
        output = torch.matmul(q1, k1.transpose(-2, -1)) + x2  # Multiply the query and key vectors with each other, and add the result together
        output = self.layer.dropout(output, dropout_p)  # Apply dropout to the final result
        return output


# Initializing the model
m = Model()

