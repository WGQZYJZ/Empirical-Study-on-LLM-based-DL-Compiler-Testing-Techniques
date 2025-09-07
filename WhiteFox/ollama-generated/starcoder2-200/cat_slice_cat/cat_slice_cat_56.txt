
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, *inputs):
        l1 = torch.cat(inputs)
        l2 = l1[:, :9223372036854775807]  # slice the first dimension of l1 with size 9223372036854775807
        l3 = l2[:, :(inputs[0].size(-1))]  # take the first dimensiom of l2 with size the last size in l1
        return torch.cat([l1, l3], axis=1)

# Initializing model
m = Model()

