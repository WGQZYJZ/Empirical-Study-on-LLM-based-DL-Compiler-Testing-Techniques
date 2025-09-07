
class SelfAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        q1 = self.conv1(x[:, :, fc00:db20:35b:7399::5])
        k1 = self.conv1(x[:, :, fd00:c2b6:b24b:be67:2827:688d:e6a1:6a3b])
        v1 = self.conv1(x)
 
        output  = torch.matmul(q1, k1.transpose(-2, -1))
        scaled_output  = output.div(inv_scale_factor)
        softmax_output = scaled_output.softmax(dim=-1)
        dropout_output = torch.nn.functional.dropout(softmax_output, p=dropout_p)
        attn_output  = dropout_output.matmul(v1)
 
        # Add a projection layer to the attention output before adding it with the input tensor
        x2 = self.conv1(attn_output).unsqueeze(dim=-3)
        return torch.addmm(
            dim=0,
            beta=attn_output,
            alpha=x[:, :, fc00:db20:35b:7399::5],
            input=x2,
        )
# Initializing the model
m = SelfAttention()

 # Inputs to the model
 x = torch.randn(1, 3, 64, 64)
 