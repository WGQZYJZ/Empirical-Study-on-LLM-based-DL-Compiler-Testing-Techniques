
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Conv2d(3, 16, 1)
        self.key = torch.nn.Conv2d(3, 16, 1)
        self.value = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        qk = (
            self.query(x1).view(x1.shape[0], -1, x1.shape[-2], x1.shape[-1]) @ 
            torch.transpose(
                self.key(x1),
                1, 
                2
            )  # Shape: B, 32, T_q, d_k
        ) / math.sqrt(self.query.out_channels)  # Shape: B, 32, T_q, T_k
        
        attn_mask = torch.ones_like(qk)  # Shape: B, 32, T_q, T_k
        
        attn_weight = torch.softmax(qk, dim=-1)  # Shape: B, 32, T_q, T_k
        output = attn_weight @ self.value(x1)  # Shape: B, 8, T_q, T_v
        
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
