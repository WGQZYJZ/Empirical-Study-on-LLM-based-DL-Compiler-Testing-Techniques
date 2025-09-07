
class Model(torch.nn.Module):
    def __init__(self, size=50):
        super().__init__()
 
    def forward(self, *inputs):
        v3 = torch.cat([v2[:, :size], inputs[1][input_idx][None]], dim=1) # input tensor shape 1, size, 9223372036854775807
        return [v3]


# Initializing the model