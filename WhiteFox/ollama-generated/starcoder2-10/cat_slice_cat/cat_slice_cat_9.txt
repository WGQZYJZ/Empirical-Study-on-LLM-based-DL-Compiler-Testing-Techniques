
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(9223372036854775807, 1)
 
    def forward(self, x1): # In this example we will consider input tensor size to be 9223372036854775807
        v1 = torch.cat([x1[:, :, :], x1[:, :, 1:]], dim=2)
        v2 = v1[:][torch.randperm(v1)]
        v3 = v2[torch.randint(size=(9223372036854775807,), high=v1.shape[-1])]
        v4 = torch.cat([x1[:, :, :], x3,], dim=2)  # size(v3) = (batch_size, size, 1)
        v5 = self.fc(v4[:, :, -9223372036854775807:])   # 9223372036854775807 is used as size
        return v5

# Initializing the model with random inputs
m = Model()
x1 = torch.randn(1, 3, 9223372036854775807)

