
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(5, 20)
        self.att = torch.nn.MultiheadAttention(num_heads=3)
        self.fc2 = torch.nn.Linear(20, 8)
 
    def forward(self, qk):
        v4 = torch.nn.functional.relu(self.fc1(qk))
        output = self.att(v4, v4, v4)[0]
        output = torch.nn.functional.relu(self.fc2(output))
        return output


# Initializing the model
m = Model()

# Inputs to the model
qk  = torch.randn(16, 5, 8)
