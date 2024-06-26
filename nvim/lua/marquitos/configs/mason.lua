local M = {}

M.options = function()
    local options = {
        PATH = "prepend",

        max_concurrent_installers = 10,
    }

end

M.lsp_defaults = function()

    require("mason-lspconfig").setup({

        ensure_installed = {
            "lua_ls",
            "gopls",
            "pyright",
            "dockerls",
            "docker_compose_language_service",
            "bashls",
            "lemminx",
            "phpactor",
            "tsserver"
        },

        handlers = {
            function(server_name)
                require("lspconfig")[server_name].setup { capabilities = capabilities }
            end
        },
        settings = {
            Lua = {
                diagnostics = {
                    globals = { 'vim','diagnostics', 'capabilities' }
                }
            }
        }
    })

end



return M


