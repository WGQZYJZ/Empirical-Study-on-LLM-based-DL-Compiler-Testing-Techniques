
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.query = torch.nn.Linear(32, 10)
        self.key   = torch.nn.Linear(32, 8)
        self.value = torch.nn.Linear(456, 90)

    def forward(self, query):
        # Input query tensor of shape (N, T_q, F), where N is the batch size,
        # and T_q is the number of queries in the batch, and F is a feature vector length.
        key   = self.key  (query)
        value = self.value(query)

        # Compute the dot product of the query tensor with each key tensor. This
        # results in an output of shape (N, T_q, T_k). Then compute the scaled
        # dot product by using the temperature scale factor. After scaling, it is
        # possible to take the softmax of this tensor as there are many values that 
        # will all be negative and therefore add up to 0. Therefore a divide by
        # the maximum value in each tensor makes the tensors much more manageable.
        dot   = torch.bmm(query, key.transpose(-2,-1)) / self._scale_factor

        # Compute dropout of the softmax output, which results in an output of shape (N, T_q, T_k)
        drop  = torch.nn.functional.dropout(softmax(dot), p=self.drop_p)

        # Finally compute dot product of the value tensor and dropout
        out   = drop @ value
        
        return out

# Initializing the model. The temperature factor is set to 32.
m = AttentionModel()


# Inputs to the model: Input query tensor that contains 16 input vectors with each vector length being 32 units long.
x1_qry  = torch.randn(8, 50, 32) # Input query of shape (N, T_q, F), where N is the batch size and T_q is the number of queries in the batch and F is a feature vector length.
x1__out = m(x1_qry)

