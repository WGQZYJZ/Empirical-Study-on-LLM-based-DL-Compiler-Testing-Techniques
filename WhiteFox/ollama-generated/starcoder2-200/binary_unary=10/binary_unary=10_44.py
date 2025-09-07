
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(6400, 1)
        self.other = torch.tensor([2])
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 + other
        v3 = relu(v2)
        return v3

# Initializing the model and inputs to the model
m  = Model()
x  = torch.randn(4096, 1).to(device='cuda')

 # Initializing the target model and inputs to the target model
    m_target  = torch.load("model.pt") 
    x_target  = torch.randn(4096)

# Saving the model
torch.save(m, "model.pt")