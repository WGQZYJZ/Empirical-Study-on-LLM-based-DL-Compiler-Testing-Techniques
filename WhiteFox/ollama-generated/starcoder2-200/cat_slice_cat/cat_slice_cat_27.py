

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input):
        t = torch.cat(input, dim=1) # Concatenate tensors along dimension 1
        return t[:, :size]


# Initializing the model
m = Model()

# Inputs to the model
input_tensors = [
    torch.randn([3, 256]),
    torch.randn([4, 9])
]
