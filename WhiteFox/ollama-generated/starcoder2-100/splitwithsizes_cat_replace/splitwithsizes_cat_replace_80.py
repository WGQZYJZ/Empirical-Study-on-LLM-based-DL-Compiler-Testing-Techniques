
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, x1, y2):
        v0  = torch.split(x1[0], [3], dim=1) # Split the first channel of the input tensor into two tensors along dimension 1 using split
        v1  = torch.split(y2[0], [48], dim=0)[0] # Split the first batch from the second channel of the input tensor into a single tensor using split
        v3  = torch.cat([v0[0].reshape(1, 4), v0[1]], axis=-2) + 64 * v1# Concatenate two tensors along dimension 1 and add 64 times the second channel of the input tensor to each resulting element using cat
        return torch.split(v3, [5], dim=0)[0]  # Split the concatenated tensor along dimension 0


# Initializing the model
m = Model()


# Inputs to the model
__output__  = m(torch.randn([1, 8, 24, 64]), torch.randn([3, 75]))