
class TransformerModel(torch.nn.Module):
    def __init__(self, config):
        super().__init__()

        self.d_model = config['d_model']  # The dimensionality of the hidden layer in the feedforward layer
        self.nhead = config["num_heads"]  # Number of attention heads
        
        