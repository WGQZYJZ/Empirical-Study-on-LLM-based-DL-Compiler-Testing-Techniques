
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention_layer = torch.nn.Linear(768, 512) # Linear layer that maps to a query-key matrix (Q,K), where Q and K are the outputs of convolutional layers.

    def forward(self, x1, key):
        qk = torch.matmul(x1, key.transpose(-2, -1)) # Compute the dot product of the query and the key

        scaled_qk = qk / 0.7071067811865476 # Scale the dot product by the inverse scale factor
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5) # Apply dropout to the softmax output

        output = self.attention_layer(dropout_qk) # Compute the dot product of the dropout output and a key

        return x1 * 0.8


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
key = torch.randn(2, 768, 56, 56) # key's shape is (bs=2, dim=768, height=56, width=56)
