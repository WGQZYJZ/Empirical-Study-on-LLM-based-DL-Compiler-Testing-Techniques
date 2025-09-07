
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, num_heads=8, input_dim=16, query_dim=32, key_dim=32):
        super().__init__()
        self.num_heads = num_heads
        
        