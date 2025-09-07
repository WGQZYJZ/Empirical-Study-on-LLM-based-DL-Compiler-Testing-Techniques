
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(20, 8)
 
    def forward(self, q1, k1):
        v1 = torch.matmul(q1, k1.transpose(-2, -1))
        v2 = v1 * scale_factor
        v3 = v1.softmax(dim=-1)
        v4 = torch.nn.functional.dropout(v3, p=dropout_p)
        output = v4.matmul(value)
        return output


# Initializing the model
m = Model()

# Inputs to the model
q1  = torch.randn(8, 20, 16, 64)
k1  = torch.randn(8, 20, 32, 64)
