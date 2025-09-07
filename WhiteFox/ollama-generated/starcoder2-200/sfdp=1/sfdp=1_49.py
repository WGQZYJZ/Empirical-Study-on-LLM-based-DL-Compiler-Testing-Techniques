
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key = torch.nn.Linear(5, 8)
 
    def forward(self, x1):
        v1 = torch.matmul(query, key.transpose(-2, -1))
        v2 = v1 / scale_factor
        v3 = scaled_qk.softmax(dim=-1) 
        v4 = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        v5 = v4.matmul(value)
        return v5


# Initializing the model
m  = Model()

 # Inputs to the model
query = torch.randn(1280, 5)
key   = torch.randn(196, 5)
value = torch.randn(32768, 1480)

 