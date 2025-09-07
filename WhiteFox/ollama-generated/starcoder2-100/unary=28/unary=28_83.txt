
class Model(torch.nn.Module):
    def __init__(self, min_value=0.1234567890123456, max_value=1.5791e+57):
        super().__init__()
        self.linear = torch.nn.Linear(20, 30)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value=min_value) 
        v3 = torch.clamp_max(v2, max_value=max_value) # This value can be obtained with 1.5791e+57
        return v3

# Initializing the model and getting its parameter count
m = Model()
total_param_count = sum([param.nelement() for param in m.parameters()])


