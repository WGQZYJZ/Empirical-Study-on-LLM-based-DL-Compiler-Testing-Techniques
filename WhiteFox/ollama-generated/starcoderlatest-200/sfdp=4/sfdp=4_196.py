
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query_conv = torch.nn.Conv2d(3, 16, 5, stride=3, padding=2)
        self.key_conv   = torch.nn.Conv2d(3, 8, 4, stride=2, padding=1)
 
    def forward(self, x1):
        qk = (
            torch.nn.functional.adaptive_avg_pool2d(
                self.query_conv(x1), 
                output_size=(64,)
            ) @ 
            self.key_conv(x1).transpose(-2, -1) / 
            math.sqrt(self.query_conv.out_channels)
        ) + 1 # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weight @ self.key_conv(x1) # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
