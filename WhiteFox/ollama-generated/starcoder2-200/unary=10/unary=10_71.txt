
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(512, 4)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + 3
        v3  = torch.clamp_min(v2, 0)
        v4  = torch.clamp_max(v3, 6)
        return v4 / 6

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(8,512)


__output__  = m(x1)

The following PyTorch functions/methods are allowed: torch.tanh, torch.clip_max, torch.softmax, torch.sigmoid, torch.cat, torch.nn.functional.one_hot (only torch.nn.functional is allowed), torch.nn.functional.pad2d, torch.nn.CrossEntropyLoss

