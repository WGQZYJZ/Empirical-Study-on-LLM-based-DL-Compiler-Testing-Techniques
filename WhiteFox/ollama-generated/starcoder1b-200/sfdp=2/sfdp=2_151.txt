
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(512, 512)
 
    def forward(self, query, key, value, mask=None):
        if mask is not None:
            assert (mask == ((mask == 0).float()).unsqueeze(2)).all(), 'Mask size is different from input.'
        # ...


# Inputs to the model
query = torch.randn(1, 512)  # Batch x SeqLen x Feature
key   = torch.randn(1, 512)  # Batch x SeqLen x Feature
value = torch.randn(1, 512)  # Batch x SeqLen x Feature
