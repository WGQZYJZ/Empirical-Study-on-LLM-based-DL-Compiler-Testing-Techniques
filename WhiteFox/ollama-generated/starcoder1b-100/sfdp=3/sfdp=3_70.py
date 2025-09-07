
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(d_model, d_k)
        self.scale_factor = torch.sqrt(torch.FloatTensor([d_k ** -0.5]))
        self.softmax = torch.nn.Softmax(dim=-1)
        self.dropout = torch.nn.Dropout(p=dropout_p)
        self.v = torch.nn.Linear(d_k, d_v)
 
    def forward(self, q, k, v):
        # Scale the dot product by a factor, and softmax it:
        scaled_qk = self.qk(q).mul(self.scale_factor)  # No transpose here!
        softmax_qk = scaled_qk.softmax(-1)  # No transpose here!
        dropout_qk = self.dropout(softmax_qk)  # Dropout!
        output = dropout_qk.matmul(v)  # Multiply by the value tensor:

        return output


# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(1, d_model)
key = torch.randn(2, d_k)
value = torch.randn(2, d_v)
