
class Model(torch.nn.Module):
    def __init__(self, dim_model=8, num_layers=1, num_heads=2, drop=0.3):
        super().__init__()
        self.dim = dim_model
        self.num_layers = num_layers
        self.num_heads = num_heads
        self.drop = drop

        self.qkv = torch.nn.Linear(dim_model, dim_model*4)  # Initialize query and key vectors for dot product
        self.mlp = nn.Sequential(
            nn.Dropout(p=self.drop),
            nn.Linear(dim_model*4, dim_model)
        )

    def forward(self, x):
        x = self.qkv(x).contiguous()  # Transform from (batch_size * channel_num * input_width * input_height) to (batch_size * head_num * dim * dim)

        x = self.mlp(x)  # Compute output after MLP

        return x

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(2, 3, 64, 64)
