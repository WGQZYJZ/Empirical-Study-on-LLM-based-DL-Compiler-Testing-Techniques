
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Conv2d(16, 32, 1, stride=8)
 
    def forward(self, x):
        qk = torch.matmul(self.query(x), x.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk = qk / 4
        softmax_qk = scaled_qk.softmax(dim=-1)
        output = torch.nn.functional.dropout(softmax_qk, p=0.3)
        return output


# Initializing the model
m = Model()
 
# Inputs to the model
x = torch.randn(16, 16, 64, 64)
