
class Model(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
 
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.fc = nn.Linear(7 * 49 * 8 , 50 )
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v_flattened  = v1.permute(2,3).reshape(-1,v1.size(1)) 
        v3  = v_flattened @ self.fc.weight.t() + self.fc.bias
        return torch.nn.functional.softmax(torch.sigmoid(v3), dim=-1)


# Initializing the model
m = Model({...})

# Inputs to the model
x2  = torch.randn(1, 3, 64, 64)
 
__output__  = m(x2)