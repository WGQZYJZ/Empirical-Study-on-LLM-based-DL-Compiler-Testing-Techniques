
class Model(torch.nn.Module):
    def __init__(self, in_dim, out_dim, num_layer=2, hidden_size=16):
        super().__init__()
        self.num_layers = 3
 
    def forward(self, x1):
        # Insert a fully connected layer with input and output dimensions of `in_dim` and `out_dim`, respectively, and number of layers in the specified list of layers: [1, num_layer]
        t1 = torch.addmm(x1, w1, b1)
        t2 = torch.cat([t1], dim)
 
        # Repeat this pattern for the next n-layers (n = 3), each with an input and output dimension of `hidden_size`
        for i in range(num_layer - 2):
            t1 = torch.addmm(t2, w2, b2)
            t2 = torch.cat([t1], dim)
 
        # Finally, insert a final fully connected layer with input and output dimensions of `out_dim` and number of layers in the specified list of layers: [1, num_layer]
        t3 = torch.addmm(t2, w3, b3)
        return t3


# Initializing the model
m = Model(64, 100, num_layer=5, hidden_size=8)
 
 # Inputs to the model
x1 = torch.randn(batch_size, 64, 128, 128)
