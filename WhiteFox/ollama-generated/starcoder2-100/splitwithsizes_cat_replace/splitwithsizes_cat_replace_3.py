
class Model(torch.nn.Module):
    def __init__(self, n_channels=32):
        super().__init__()
        self.split = torch.nn.Conv2d(n_channels, 8, kernel_size=(1, 7))

    def forward(self, x):
        t0, t1, t2 = torch.split(x, [49, 56], dim=3) # Split input into three tensors along dimension 3: t0 has size (N, C, 14, 8), t1 has size (N, C, 14, 7), and t2 has size (N, C, 14, 9).
        v1 = torch.split(self.split(t0), [36, 5], dim=1)[0] # Split t0 into two tensors along dimension 1: first tensor is of size (N, 8, 14, 7) and second is of size (N, 12, 14, 9).
        t3 = torch.cat([v1[i].squeeze(dim=2) for i in range(len(t0))], dim=1) # Concatenate the first tensor along dimension 1, and then remove its batch size of size (N, 8, 7), resulting in tensors with sizes (N, 36, 7). Similarly concatenate the second tensor.
        t4 = torch.split(t2, [5], dim=2)[0] # Split third tensor along dimension 1: first half has size (N, C, 8) and second half has size (N, C, 9).
        return torch.cat([t3.squeeze(), t4.squeeze()], dim=-1), v1

# Initializing the model
m = Model()

