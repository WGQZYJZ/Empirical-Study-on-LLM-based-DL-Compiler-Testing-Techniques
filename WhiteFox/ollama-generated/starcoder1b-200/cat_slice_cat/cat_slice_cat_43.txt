
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(3, 2)
 
    def forward(self, x1):
        y1 = torch.zeros(x1.size(0), x1.size(1), 3).to(device)
        for i in range(y1.shape[1]):
            v1 = self.fc(t1[:, :, i])
            y1[:, :, i] = v1 + 2 * v3
        return y1


# Inputs to the model
x1 = torch.randn(1, 1)
