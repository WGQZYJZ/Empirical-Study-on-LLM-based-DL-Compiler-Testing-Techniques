
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m = Model()
m_clone  = Model() # A new instance of the model with a clone of its state dict
m.load_state_dict(m_clone.state_dict()) # Load another model into the first one’s memory

