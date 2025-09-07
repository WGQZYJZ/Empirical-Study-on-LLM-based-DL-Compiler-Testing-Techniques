
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.Linear(768, 3072)
 
    def forward(self, q1, k1, v1):
        output = attention_weights(q1, k1, v1).matmul(v1)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(32, 768)
k1 = torch.randn(32, 768)
v1 = torch.randn(32, 768)
