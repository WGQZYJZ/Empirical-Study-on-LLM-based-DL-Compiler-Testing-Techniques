class SelfAttentionModel(torch.nn.Module):
    def __init__(self, inv_scale_factor=4., dropout_p=0.1) -> None:
        super().__init__()

        self._attention = torch.nn.Linear(256, 256)
        self._query = torch.nn.Linear(256, 256)
        self._key = torch.nn.Linear(256, 256)
        self._dropout = torch.nn.Dropout(dropout_p=dropout_p)

    def forward(self, data):

        v1 = self._attention(data) # Apply linear transformation to the input tensor and add bias
        v2 = v1 * inv_scale_factor  # Scale the output of the linear transformation by an inverse scale factor
        v3 = torch.nn.functional.normalize(v2, dim=0) # Apply L2 normalization
        v4 = self._query(data).transpose(-2, -1)  # Apply the query operation to the input tensor and then transpose
        v5 = v4 * inv_scale_factor   # Scale the output of applying a query operator by an inverse scale factor
        v6 = torch.nn.functional.normalize(v5, dim=0)  # Apply L2 normalization
        v7 = self._key(data).transpose(-2, -1)  # Apply the key operation to the input tensor and then transpose
        v8 = v7 * inv_scale_factor   # Scale the output of applying a query operator by an inverse scale factor
        v9 = torch.nn.functional.normalize(v8, dim=0)  # Apply L2 normalization
        v10 = torch.matmul(data, v3.transpose(-1, -2)) + v6 * v9   # Compute the dot product of the input tensor and the output of applying L2 normalization
        v11 = self._dropout(v10).softmax(dim=-1)  # Apply dropout to the dot product
        v12 = torch.nn.functional.normalize(data, dim=0) * data  # Apply L2 normalization
        v13 = v6.matmul(v9).transpose(-2, -1) + v12   # Compute the dot product of applying a query operator to the input tensor and then transposing it

        return torch.nn.functional.normalize(data, dim=0) * (
                self._dropout(torch.softmax((data @ v3.transpose(-1, -2)).div(inv_scale_factor).mul_(v7.mul_(self._key(data)).div(inv_scale_factor)), dim=-1)).matmul(
                        v8.div(self._query(data).div(inv_scale_factor))).softmax(dim=0)) + self._dropout(
            torch.nn.functional.normalize(v3, dim=0) * ((torch.nn.functional.normalize(v7, dim=-2) @ 
                                                            (1 / inv_scale_factor * v6.div_(self._key(data).div(inv_scale_factor)) * torch.nn.functional.normalize(v9, dim=-1))).softmax(-3, -1)).sum(-3).div_(torch.tensor([4]).to(data.device)), 
                                                                                                        dim=0)).matmul(
                    v7.div(self._key(data).div(inv_scale_factor))))

# Initializing the model
model = SelfAttentionModel()


# Inputs to the model
data = torch.randn(4, 256) 

