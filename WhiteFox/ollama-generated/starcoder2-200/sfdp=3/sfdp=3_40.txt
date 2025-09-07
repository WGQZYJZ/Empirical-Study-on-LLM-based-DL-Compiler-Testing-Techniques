
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = torch.nn.Parameter(1e-6)
        self.dropout = torch.nn.Dropout2d(0.3, inplace=True)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
        qk  = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk  = qk * self.scale
        softmax_qk  = scaled_qk.softmax(dim=-1)
        dropout_qk  = self.dropout(softmax_qk)
        output  = dropout_qk.matmul(value)
        return output


# Initializing the model
m = Model()
m2 = copy.deepcopy(m) # Use deepcopy to ensure that the inputs do not share storage with the model weights and bias. This ensures that we do not modify the state of our model in a way that is visible through the model's inputs and outputs.
# Generate the inputs for the model m.
query1 = torch.rand(2, 3)
key1 = torch.rand(2, 3, 5)
value1 = torch.rand(2, 5)
query1_out = m(query1, key1, value1)

 # Generate inputs for model m using the same initial weights and bias as in Model m but without copying them.
query2 = torch.rand(2, 3)
key2 = torch.rand(2, 3, 5)
value2 = torch.rand(2, 5)

# Initializing the model with new parameters
new_params  = torch.nn.ParameterDict({
    'scale': torch.nn.Parameter(1e-7), 
    'dropout':torch.nn.Dropout2d(0.3)})
m2.__init__(new_params) # Use __init__ to set the initial state of the model and initialize its weights, bias, etc., using new parameters. This will reset its internal state such that it is ready for inference with a new set of inputs.
query1 = torch.rand(2, 3)
key1 = torch.rand(2, 3, 5)
value1 = torch.rand(2, 5)
m2._modules['dropout'].__setattr__('p', 0.6) # Set the dropout parameter of the model m to a new value before computing its output with the new inputs. This will cause the model's internal state to be updated and re-used for inference using different inputs.
query3_out = m2(query1, key1, value1)

 