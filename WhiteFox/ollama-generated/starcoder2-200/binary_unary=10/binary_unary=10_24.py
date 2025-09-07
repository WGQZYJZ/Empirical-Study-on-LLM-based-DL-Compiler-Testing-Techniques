
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 64 ** 2, 10)
 
    def forward(self, x):
         v1 = self.linear(x)
         v2 = v1 + other # You can choose another tensor other. 
         return nn.functional.relu(v2),

# Initializing the model