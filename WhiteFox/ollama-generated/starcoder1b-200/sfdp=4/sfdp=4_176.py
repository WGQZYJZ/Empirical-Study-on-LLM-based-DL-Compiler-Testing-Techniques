
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.dropout = torch.nn.Dropout(p=0.5)
        self.linear_key = torch.nn.Linear(64*64*8, 256)

    def forward(self, x1, x2):
        # Compute the dot product of the query and key tensors (same dimensions as inputs),
        # scale them to avoid divide-by-zero, and add the attention mask to the scaled dot product.
        vq = self.dropout(x1 @ x2)  # This is the same as x1 @ x2, but the division by sqrt is prevented
        vq = vq + (x2 @ torch.sign(vq)).unsqueeze(-1).expand_as(vq)  # Add padding to the scaled dot product

        # Compute the weighted sum of the value tensor, using the attention weights.
        # This operation is done in the forward pass because of how dropout is implemented, but this could be easily modified to do in the backward pass instead.
        vv = torch.sum(self.conv(x2) * vq, dim=-1).squeeze(-1)  # The attention weights are only used in the computation of the weighted sum

        return vv
