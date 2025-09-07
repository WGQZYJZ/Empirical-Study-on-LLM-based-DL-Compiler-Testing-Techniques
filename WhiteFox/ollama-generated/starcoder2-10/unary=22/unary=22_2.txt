
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(256, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1) 
        v2 = torch.tanh(v1)
        return v2
 
# Initializing the model and printing the number of trainable parameters in each layer
m_model = Model()
print(f"The number of trainable parameters in the model is {sum([param.numel() for param in m_model.parameters()])}")

