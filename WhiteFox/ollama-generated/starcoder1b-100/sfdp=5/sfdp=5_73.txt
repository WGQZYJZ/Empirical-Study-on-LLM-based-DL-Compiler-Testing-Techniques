
class Model(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
 
        self.self_attn = SelfAttention(config)
        self.feed_forward = FeedForward(config)
 
    def forward(self, x1, x2):
        # Compute the dot product of the two inputs
        v1, v2 = self.self_attn(x1, x2, x1, x2)
 
        # Compute the output of the feed-forward layer
        v1  = self.feed_forward(v1)
        return v1
 

# Initializing the model
m = Model(...)


