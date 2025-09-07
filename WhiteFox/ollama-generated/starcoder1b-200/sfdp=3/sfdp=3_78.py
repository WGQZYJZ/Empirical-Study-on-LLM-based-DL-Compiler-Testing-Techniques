
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(768, 1024)
 
    def forward(self, x1):
        x_shape = x1.size()
        bsz = x_shape[0]
        x1 = x1.view(bsz, -1, 768)  # Unfold into batch and features
        query = self.qkv(x1[:, :768])  # Extract the first 768-dimension tensors from the input batch

        key = self.qkv(x1[:, 768:9216])
        value = self.qkv(x1[:, 9216:])
        # Extracting the shape of the feature vectors (query and key tensor are of dimensions 1024)
        # Multiplying the query and key tensor by a factor (scale_factor = 1)
        # Applying softmax on the scaled dot product of the features
        dropout_qk = torch.nn.functional.dropout(x=x, p=self.drop_p)
        output = (query @ key).mul(scale_factor)  # Multiplying the result with a scalar

        # Applying dropout to the result
        output = output.mul(dropout_p)
        return output


# Initializing the model
m  = Model()


