
class Model(torch.nn.Module):
    def __init__(self, d_model=512):
        super().__init__()
        self.linear = torch.nn.Linear(d_model * 3, d_model)
 
    def forward(self, x1, x2, key=None):
        attention = torch.matmul(x2.transpose(-2, -1), x1)
        scaled_attention = F.softmax(attention / (key.shape[-1] ** 0.5), dim=-1) # Compute softmax on the last axis
        return self.linear(scaled_attention).unsqueeze(1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
key = torch.randn(1, 8, 64, 64)
