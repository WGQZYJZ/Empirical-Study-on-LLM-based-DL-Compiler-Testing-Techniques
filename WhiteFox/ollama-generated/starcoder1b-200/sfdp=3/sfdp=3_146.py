
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(d_model, d_k)
        self.key   = torch.nn.Linear(d_model, d_k)
        self.value = torch.nn.Linear(d_model, d_v)

    def forward(self, x):
        # 1. Compute dot products of input and key
        q = self.query(x).reshape((batch_size, seq_length, -1))
        k = self.key(x).reshape((batch_size, seq_length, -1))
        
        # 2. Scale dot product to match d_k
        q *= torch.div(d_k ** (-0.5), self.d_k)

        # 3. Apply softmax over all dimensions of the dot product,
        #   then calculate dropout (training only)
        dropout_qk = torch.nn.functional.softmax(q, dim=-1).unsqueeze(-1) * x
        # Dropout is only performed in training mode;
        # in inference mode it is not applied and the values are unaffected.

        # 4. Compute value tensors and linear layers
        output = dropout_qk.matmul(self.value(x))
        
        # 5. Return output and last hidden state
        return output, torch.tanh(output)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__, __hidden__ = m(x1)


