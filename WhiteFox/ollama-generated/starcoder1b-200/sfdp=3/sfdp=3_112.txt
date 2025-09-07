
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1d = torch.nn.Conv1d(3, 8, kernel_size=5, stride=1, padding=2)

    def forward(self, x1):
        # Calculate the dot product of x and self.padding_mask
        qk  = torch.matmul(x1, self.padding_mask.unsqueeze(-2).unsqueeze(-1))

        # Scale and apply dropout to output
        scaled_qk = qk.mul(scale_factor)
        dropout_qk = torch.nn.functional.dropout(scaled_qk, p=dropout_p)

        # Compute the dot product of x with attention weights
        value  = dropout_qk.matmul(value)

        # Apply attention on a reduced version of the query tensor
        output = self.attention(x1, scaled_qk, query_mask, value_mask)

        return output


# Initializing the model
m = Model()


