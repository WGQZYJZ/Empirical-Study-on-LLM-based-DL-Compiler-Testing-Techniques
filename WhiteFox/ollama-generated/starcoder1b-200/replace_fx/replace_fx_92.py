# Description of requirements
The model should contain the following pattern:
This pattern characterizes scenarios where the input tensor is not a tensor but contains elements with integer indices, or the output of an arithmetic operation is passed in as a scalar value. The node that invokes 'flatten' on the first three dimensions will be erased from the graph. Also, the `gm.graph.erase_node(node)`) function will erase nodes that do not contain 'input_tensor'.

Note that if the model requires gradient inputs (e.g., LSTM), or uses `require_grad`, the node invoking this function will be erased from the graph as well.


# Model
class Model(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.rnn = torch.nn.RNN(...)  # An instance of class RNN

    def forward(self, input_tensor):
        output, _ = self.rnn(input_tensor)
        return output
if config['mode'] == 'eval':
    with torch.no_grad():
        v1 = input_tensor[:, :2]
        for i in range(config['batch_size']):
            output = ...  # Calculate something.
            hidden = self._last_hidden_state[i][:, :, :-1]
            new_input = ...  # Calculate something else.
            next_hidden = self._rnn_cell(new_input, hidden)
            self._last_hidden_state[i][:, :, -1] = next_hidden
        return output
{
    "batch_size": 3,
    "mode": "eval"
}
