return{
    {
        "williamboman/mason.nvim",
        cmd = { "Mason", "MasonInstall", "MasonInstallAll", "MasonUpdate" },
        opts = function()
            require "marquitos.configs.mason".options()
        end

    },

    {
        "williamboman/mason-lspconfig.nvim",
        config = function()
                require('marquitos.configs.mason').lsp_defaults()
        end
    }
}
