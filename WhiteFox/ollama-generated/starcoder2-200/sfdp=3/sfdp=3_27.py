{
    "model": [
        {
            "name": "__main__.Model",
            "inputs": [],
            "outputs": [],
            "ops": ["torch.nn.modules.conv.Conv2d", 
                   "torch.matmul", 
                   "torch.nn.functional.dropout", 
                   "torch.nn.modules.linear.Linear"],
            "params": [{"name": "__class__", 
                        "type": "str",
                        "value": "<class 'torch.nn.modules.conv._ConvNd'>"},
                       {"name": "_backend_module_", 
                       "type": "str",
                      "value": ""}, 
                      {"name": "__init__.<locals>._make_args_helper", 
                        "type": "",
                       "value": "[(1,), <class 'torch.nn.modules.utils.ConvOptions'>, 25, 'cudnn_autotuner']"}]
        },
        {
            "name": "<function Model.__init__ at 0x1358b9a60>", 
            "inputs": [], 
            "outputs": [
                        {"name": "__class__", 
                        "type": "str",
                       "value": "<class 'torch.nn.modules.conv._ConvNd'>"},
                       {"name": "_backend_module_", 
                       "type": "str",
                      "value": ""}, 
                      {"name": "__init__.<locals>._make_args_helper", 
                        "type": "",
                        "value": "[(1,), <class 'torch.nn.modules.utils.ConvOptions'>, 25, 'cudnn_autotuner']"}
                       ]
        },
        {
            "name": "<function Model.__init__.<locals>._make_args_helper at 0x1358b75e0>", 
            "inputs": [
                        {"name": "__class__", 
                        "type": "str",
                       "value": "<class 'torch.nn.modules.conv._ConvNd'>"},
                       {"name": "_backend_module_", 
                       "type": "str",
                      "value": ""}, 
                      ],
            "outputs": [], 
            "ops": ["__torch__.torch.nn.modules.conv._ConvNd.__init__", 
                    "__torch__.torch._C._jit_script_unpickling_executor"],
            "params": [
                        {"name": "_backend_", 
                        "type": "str",
                       "value": ""}, 
                      ]
        }
    ],

