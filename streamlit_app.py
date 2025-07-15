<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🔍 Soufian Search - Excel Product Finder</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script>
    <style>
        :root {
            --primary-color: #2b67f6;
            --secondary-color: #1e4bff;
            --light-color: #f8faff; /* Lighter blue */
            --dark-color: #1a1a2e;
            --success-color: #4caf50;
            --footer-color: #666;
            --table-border-color: #ddd;
            --background-color: white;
            --text-color: #333;
        }

        body {
            background-color: var(--light-color);
            color: var(--text-color);
            line-height: 1.6;
            padding: 20px;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            background-color: var(--background-color);
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            padding: 30px;
        }

        h1 {
            color: var(--primary-color);
            text-align: center;
            font-weight: bold;
            font-size: 24px;
            margin-bottom: 20px;
        }

        .app-description {
            text-align: center;
            margin-bottom: 30px;
            color: #555;
        }

        .file-upload-section {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-bottom: 30px;
            padding: 20px;
            border: 2px dashed var(--secondary-color);
            border-radius: 12px;
            background-color: #f9f9f9;
        }

        .file-upload-btn {
            background-color: var(--primary-color);
            color: white;
            padding: 15px 30px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 18px;
            font-weight: 500;
            transition: background-color 0.3s;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .file-upload-btn:hover {
            background-color: var(--secondary-color);
        }

        #file-input {
            display: none;
        }

        .file-info {
            margin-top: 10px;
            font-size: 14px;
            color: #666;
        }

        .search-section {
            margin-bottom: 30px;
        }

        .search-container {
            display: flex;
            gap: 10px;
        }

        #search-input {
            flex: 1;
            padding: 15px 20px;
            border: 1px solid var(--table-border-color);
            border-radius: 8px;
            font-size: 16px;
            outline: none;
            transition: border-color 0.3s;
        }

        #search-input:focus {
            border-color: var(--primary-color);
        }

        #search-btn {
            background-color: var(--primary-color);
            color: white;
            padding: 15px 30px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 18px;
            font-weight: 500;
            transition: background-color 0.3s;
        }

        #search-btn:hover {
            background-color: var(--secondary-color);
        }

        .results-info {
            margin-top: 15px;
            font-size: 14px;
            color: #555;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .results-count {
            font-weight: 600;
            color: var(--secondary-color);
        }

        .results-section {
            overflow-x: auto;
        }

        table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            margin-top: 20px;
            border: none;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }

        th, td {
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid var(--table-border-color);
        }

        th {
            background-color: var(--primary-color);
            color: white;
            font-weight: 600;
            text-transform: uppercase;
            font-size: 14px;
        }

        tr:nth-child(even) {
            background-color: #f2f2f2;
        }

        tr:hover {
            background-color: #e0e0e0;
        }

        .no-results {
            text-align: center;
            padding: 40px;
            color: #666;
            font-size: 18px;
        }

        .loading {
            display: none;
            text-align: center;
            padding: 20px;
        }

        .loading-spinner {
            display: inline-block;
            width: 24px;
            height: 24px;
            border: 4px solid rgba(0, 0, 0, 0.1);
            border-radius: 50%;
            border-top-color: var(--primary-color);
            animation: spin 1s ease-in-out infinite;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        .footer {
            text-align: center;
            margin-top: 40px;
            font-size: 14px;
            color: var(--footer-color);
            padding-top: 20px;
            border-top: 1px solid #eee;
        }

        .logo {
            font-size: 24px;
            font-weight: bold;
            color: var(--primary-color);
            position: absolute;
            top: 20px;
            left: 20px;
        }

        .dark-mode {
            background-color: #1a1a2e;
            color: white;
        }

        .dark-mode .container {
            background-color: #2a2a3c;
        }

        .dark-mode .file-upload-btn {
            background-color: #4a6fa5;
        }

        .dark-mode th {
            background-color: #4a6fa5;
        }

        .dark-mode tr:nth-child(even) {
            background-color: #333;
        }

        .dark-mode .no-results {
            color: #ccc;
        }

        .dark-mode .footer {
            color: #aaa;
        }

        .dark-mode #search-input {
            background-color: #444;
            color: white;
            border: 1px solid #666;
        }

        .dark-mode #search-input:focus {
            border-color: #4a6fa5;
        }

        .dark-mode #search-btn {
            background-color: #4a6fa5;
        }

        .dark-mode #search-btn:hover {
            background-color: #166088;
        }

        @media (max-width: 768px) {
            .container {
                padding: 15px;
            }

            .search-container {
                flex-direction: column;
            }

            #search-btn {
                width: 100%;
            }

            th, td {
                padding: 8px 10px;
                font-size: 14px;
            }
        }
    </style>
</head>
<body>
    <div class="logo">SS</div>
    <div class="container">
        <h1 style="font-size: 2.2rem; margin-bottom: 10px;">🔍 Soufian Search</h1>
        <p class="app-description" style="font-size: 1.1rem;">
            Powerful Excel Search Tool | Find products by codes, names, departments or stock
        </p>
        
        <div class="file-upload-section">
            <input type="file" id="file-input" accept=".xlsx, .xls, .csv" />
            <button class="file-upload-btn" id="upload-btn" style="padding: 12px 24px; font-size: 16px;">
                <svg style="width:20px;height:20px;margin-right:8px;" viewBox="0 0 24 24">
                    <path fill="currentColor" d="M9,16V10H5L12,3L19,10H15V16H9M5,20V18H19V20H5Z" />
                </svg>
                UPLOAD EXCEL FILE
            </button>
            <div style="font-size:12px;color:#666;margin-top:12px;">
                Supports .xlsx, .xls (Max 10MB) • Required columns: CODE CAISSE, DESCRIPTION_ARTICLE
            </div>
            <p class="file-info">File format: Excel (.xlsx, .xls) with "CODE CAISSE", "DESCRIPTION_ARTICLE", "RAYON", "STOCK_en_QTE", "PRIX_vent" columns</p>
            <div id="file-name" class="file-info"></div>
        </div>
        
        <div class="search-section">
            <div class="search-container">
                <input type="text" id="search-input" placeholder="🔍 Search products by code, name or department..." 
                       style="padding: 12px 15px; font-size: 15px;" />
                <button id="search-btn" style="background: linear-gradient(135deg, #2b67f6 0%, #1e4bff 100%);">SEARCH</button>
            </div>
            <div class="results-info">
                <span id="match-count" class="results-count">0 products found</span>
                <span id="total-count">0 products loaded</span>
            </div>
        </div>
        
        <div class="loading">
            <div class="loading-spinner"></div>
            <p>Loading data...</p>
        </div>
        
        <div class="results-section" id="results-section">
            <div class="no-results">
                Upload an Excel file and search for products
            </div>
        </div>

        <div class="footer" style="font-size: 13px; color: #777; margin-top: 30px;">
            <div style="margin-bottom: 5px;">Made with ❤️ by Soufian</div>
            <div style="font-size: 11px; color: #aaa;">Excel Product Finder v1.0</div>
        </div>
    </div>

    <script>
        let products = [];
        let currentFile = null;

        function downloadApp() {
            const htmlContent = document.documentElement.outerHTML;
            const blob = new Blob([htmlContent], {type: 'text/html'});
            const url = URL.createObjectURL(blob);
            
            const a = document.createElement('a');
            a.href = url;
            a.download = 'Excel_Search_Tool.html';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        }

        document.addEventListener('DOMContentLoaded', () => {
            const fileInput = document.getElementById('file-input');
            const uploadBtn = document.getElementById('upload-btn');
            const searchInput = document.getElementById('search-input');
            const searchBtn = document.getElementById('search-btn');
            const resultsSection = document.getElementById('results-section');
            const fileNameElement = document.getElementById('file-name');
            const matchCountElement = document.getElementById('match-count');
            const totalCountElement = document.getElementById('total-count');
            const loadingElement = document.querySelector('.loading');

            // Upload file handler
            uploadBtn.addEventListener('click', () => {
                fileInput.click();
            });

            fileInput.addEventListener('change', async (e) => {
                const file = e.target.files[0];
                if (!file) return;
                
                try {
                    loadingElement.style.display = 'block';
                    resultsSection.innerHTML = '';
                    
                    const data = await readFile(file);
                    processExcelData(data);
                    currentFile = file;
                    fileNameElement.textContent = `Loaded: ${file.name}`;
                    totalCountElement.textContent = `${products.length} products loaded`;
                    searchInput.focus();
                    
                    // Perform initial search if there's a query
                    if (searchInput.value.trim()) {
                        searchProducts(searchInput.value.trim());
                    }
                } catch (error) {
                    console.error('Error processing file:', error);
                    resultsSection.innerHTML = `<div class="no-results">Error loading file: ${error.message}</div>`;
                } finally {
                    loadingElement.style.display = 'none';
                }
            });

            // Search handlers
            searchBtn.addEventListener('click', () => {
                const query = searchInput.value.trim();
                if (query) {
                    searchProducts(query);
                } else {
                    displayAllProducts();
                }
            });

            searchInput.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') {
                    const query = searchInput.value.trim();
                    if (query) {
                        searchProducts(query);
                    } else {
                        displayAllProducts();
                    }
                }
            });

            // Function to read Excel file
            async function readFile(file) {
                return new Promise((resolve, reject) => {
                    const reader = new FileReader();
                    reader.onload = (e) => {
                        resolve(e.target.result);
                    };
                    reader.onerror = (error) => {
                        reject(new Error('Error reading file'));
                    };
                    reader.readAsArrayBuffer(file);
                });
            }

            // Process Excel data
            function processExcelData(data) {
                const workbook = XLSX.read(data, { type: 'array' });
                const firstSheet = workbook.Sheets[workbook.SheetNames[0]];
                products = XLSX.utils.sheet_to_json(firstSheet);
                
                // Convert all values to strings for easier searching
                products = products.map(product => {
                    const processedProduct = {};
                    for (const key in product) {
                        processedProduct[key] = String(product[key]).trim();
                    }
                    return processedProduct;
                });
            }

            // Search function
            function searchProducts(query) {
                if (!products.length) {
                    resultsSection.innerHTML = '<div class="no-results">No products loaded. Please upload an Excel file first.</div>';
                    return;
                }
                
                query = query.toLowerCase();
                const matchedProducts = products.filter(product => {
                    return Object.values(product).some(value => 
                        value.toLowerCase().includes(query)
                    );
                });
                
                displayResults(matchedProducts);
                matchCountElement.textContent = `${matchedProducts.length} products found`;
            }

            // Display all products when no query
            function displayAllProducts() {
                if (!products.length) {
                    resultsSection.innerHTML = '<div class="no-results">No products loaded. Please upload an Excel file first.</div>';
                    return;
                }
                
                displayResults(products);
                matchCountElement.textContent = `Showing all ${products.length} products`;
            }

            // Display results in a table
            function displayResults(results) {
                if (!results.length) {
                    resultsSection.innerHTML = '<div class="no-results">No products match your search</div>';
                    return;
                }
                
                const table = document.createElement('table');
                
                // Create header
                const thead = document.createElement('thead');
                const headerRow = document.createElement('tr');
                
                const headers = [
                    'CODE CAISSE', 'DESCRIPTION_ARTICLE', 'RAYON', 
                    'STOCK_en_QTE', 'PRIX_vent'
                ];
                
                headers.forEach(header => {
                    const th = document.createElement('th');
                    th.textContent = header;
                    headerRow.appendChild(th);
                });
                
                thead.appendChild(headerRow);
                table.appendChild(thead);
                
                // Create body
                const tbody = document.createElement('tbody');
                
                results.forEach(product => {
                    const row = document.createElement('tr');
                    
                    headers.forEach(header => {
                        const td = document.createElement('td');
                        td.textContent = product[header] || '-';
                        row.appendChild(td);
                    });
                    
                    tbody.appendChild(row);
                });
                
                table.appendChild(tbody);
                resultsSection.innerHTML = '';
                resultsSection.appendChild(table);
            }
        });
    </script>
</body>
</html>
``` ```python
import streamlit as st
import pandas as pd

st.set_page_config(page_title="🔍 Soufian Search - Excel Product Finder", layout="wide")

st.title("🔍 Soufian Search - Excel Product Finder")
st.write("Powerful Excel Search Tool | Find products by codes, names, departments or stock")

uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx", "xls", "csv"])
if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)
        st.success(f"Loaded: {uploaded_file.name}")
        st.write(f"Total products loaded: {len(df)}")
        
        search_query = st.text_input("🔍 Search products by code, name or department...")
        
        if search_query:
            results = df[df.apply(lambda row: row.astype(str).str.contains(search_query, case=False).any(), axis=1)]
            if not results.empty:
                st.write(f"{len(results)} products found")
                st.dataframe(results)
            else:
                st.warning("No products match your search")
        else:
            st.dataframe(df)
    except Exception as e:
        st.error(f"Error loading file: {e}")

st.markdown("<div style='text-align: center; margin-top: 40px;'>Made with ❤️ by Soufian</div>", unsafe_allow_html=True)
