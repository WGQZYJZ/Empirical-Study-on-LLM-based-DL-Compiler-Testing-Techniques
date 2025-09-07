

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.randn([5]) # Permute the input tensor
        return 3, [v]

