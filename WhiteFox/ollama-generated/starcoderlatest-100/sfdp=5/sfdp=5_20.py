
class Model(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
        self.d_model = config['d_model']
        self.num_heads = config['num_heads']
        # Number of channels for the first convolution
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
        self.norm1 = torch.nn.LayerNorm([8])

        # Two blocks of transformer layers
        self.layers = nn.Sequential()
        for i in range(2):
            block_layers = nn.Sequential()
            block_layers.add_module('attn', SelfAttention(config))
            block_layers.add_module('ff', FeedForward(config))
            self.layers.add_module('block' + str(i), block_layers)
        # The output layer
        self.out = torch.nn.Linear(2 * config['d_model'], 10)

    def forward(self, x):
        v = self.conv1(x)
        v = self.norm1(v)

        v1 = self.layers[0](v)
        for layer in self.layers:
            v1 = layer(v1)

        v2 = torch.cat([v, v1], dim=1)  # Concatenate the outputs of all transformer layers
        
        output = self.out(v2).view(-1, 10)
        
        return output


# Initializing the model
m = Model({
    'd_model': 8,
    'num_heads': 4,
})

# Inputs to the model
x = torch.randn(32, 3, 64, 64)
