// import tailwindcss from '@tailwindcss/vite';
// import react from '@vitejs/plugin-react';
// import path from 'path';
// import {defineConfig, loadEnv} from 'vite';

// export default defineConfig(({mode}) => {
//   const env = loadEnv(mode, '.', '');
//   return {
//     plugins: [react(), tailwindcss()],
//     define: {
//       'process.env.API_KEY': JSON.stringify(env.API_KEY),
//     },
//     resolve: {
//       alias: {
//         '@': path.resolve(__dirname, './src'),
//       },
//     },
//     server: {
//       hmr: process.env.DISABLE_HMR !== 'true',
//       // Disable file watching when DISABLE_HMR is true to save CPU during agent edits.
//       watch: process.env.DISABLE_HMR === 'true' ? null : {},
//     },
//   };
// });


import tailwindcss from '@tailwindcss/vite';
import react from '@vitejs/plugin-react';
import path from 'path';
import {defineConfig, loadEnv} from 'vite';

export default defineConfig(({mode}) => {
  const env = loadEnv(mode, '.', '');
  return {
    plugins: [react(), tailwindcss()],
    define: {
      'process.env.API_KEY': JSON.stringify(env.API_KEY),
    },
    resolve: {
      alias: {
        '@': path.resolve(__dirname, './src'),
      },
    },
    server: {
      hmr: process.env.DISABLE_HMR !== 'true',
      // SỬA Ở ĐÂY: Thêm ignored để Vite phớt lờ sự thay đổi của file Benchmark
      watch: process.env.DISABLE_HMR === 'true' ? null : {
        ignored: ['**/public/benchmark_result.json']
      },
    },
  };
});


