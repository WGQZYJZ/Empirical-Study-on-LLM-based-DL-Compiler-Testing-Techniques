

class AttnTransformerModel(torch.nn.Module):
    def __init__(self, config):
        super().__init__()

        # Initialize layers and get hyperparameters
        self.attn  = torch.nn.MultiheadAttention(config["num_heads"], dim=1)

        # Define dropout probability for the attention weights
        dropout = config['dropout']
        
        # ...

    def forward(self, query, key, value):
        