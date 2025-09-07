
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(128, 128, 3, stride=2, padding=1)
 
    def forward(self, x1, x2, mask_x1=None):
        v1 = self.conv(x1)
        v2 = self.conv(x2)
 
        # Add an attention mask for the padded tokens at the start and end of the sequence
        if mask_x1 is not None:
            extended_mask = torch.cat((mask_x1.unsqueeze(1),
                                        mask_x1.unsqueeze(-2)), dim=-1)
            v1 *= extended_mask
            v2 *= extended_mask
 
        # Convert padded masks into unpadded masks
        if x1.dim() == 4:
            paddings = torch.nn.functional.pad(v1, (0, 1, 0, 1), mode='reflect')
        elif x1.dim() == 5:
            paddings = v1.new_zeros([x1.size(0) * x1.size(1)]).to(device)
        # Compute the dot product between the query and key (Q k^T / ||q||||k||),
        # and scale it by a temperature parameter τ to avoid numerical instability
        attn_weights = torch.matmul(v2, v1.transpose(-2, -1)) * 0.05
        qk  = torch.softmax(attn_weights, dim=-1) * 0.05
 
        # Add the attention mask (capped at 1) to each row and column of the softmax matrix.
        # These rows/columns are scaled by a temperature parameter τ to avoid numerical instability
        if x2.dim() == 4:
            attn_weights = torch.nn.functional.pad(qk, (0, 0), mode='reflect')
        elif x2.dim() == 5:
            attn_weights = qk
        # Compute the dot product between the query and key (Q k^T / ||q||||k||),
        # and scale it by a temperature parameter τ to avoid numerical instability
        if x1.dim() == 4:
            output = torch.matmul(attn_weights, v1) * 0.05
        elif x1.dim() == 5:
            output = torch.matmul(attn_weights.view(-1, attn_weights.size(-1)), v1.transpose(-2, -1)) * 0.05
 
        return output.permute([0, 2, 3, 1])


# Inputs to the model
x1 = torch.randn(1, 4, 128, 128)
mask_x1 = torch.randint(0, 2, (1,)).to(device)
x2 = torch.randn(1, 4, 64, 64)
