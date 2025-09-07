
class SelfAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.layer_norm = torch.nn.LayerNorm(axis=-1)
 
        self.linear_keys  = torch.nn.Linear(512, 2048, bias=False)
        self.linear_values  = torch.nn.Linear(512, 2048, bias=False)
        self.linear_queries  = torch.nn.Linear(512, 2048, bias=False)
 
    def forward(self, x):
        residual = x
 
        # Linear projection to generate two new tensors with the same size
        y1 = F.relu(self.layer_norm(x), inplace=True)
        qk_linear_keys  = self.linear_keys (y1).transpose(-2, -1)
        vq_linear_values = self.linear_values(y1)
 
        # Scale by the square root of the dimensionality of the keys tensor
        y2 = F.relu(self.layer_norm(x), inplace=True)
        qk_scale_factor  = torch.einsum('bnw,bnm->bnwmn', y2, self.linear_queries(y2)) ** 0.5
        vq_scale_factor  = torch.einsum('bnm,bnw->bnwm', y2, self.linear_queries(y2)) ** 0.5
 
        # Multiply the two new tensors element-wise with their corresponding scale factors
        qk_scaled  = qk_linear_keys * qk_scale_factor
        vq_scaled  = vq_linear_values * vq_scale_factor
 
        # ReLU non-linearity to ensure that there are no negative values in the attention coefficients
        y3 = F.relu(self.layer_norm(qk_scaled), inplace=True)
        y4 = torch.einsum('bnwmn,bnwm->bnw', y3, vq_scaled)
 
        return self.layer_norm(y1 + residual*y4, inplace=True)


# Inputs to the model
x2 = torch.randn(1, 512, 64, 64)
