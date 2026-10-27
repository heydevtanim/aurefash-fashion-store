const products = [
 {id:1,name:'The everyday trench',type:'Clothing',price:248,color:'Oat',tag:'New in',image:'photo-1539109136881-3be0616acf4b',alt:'Tailored neutral outerwear in soft light'},
 {id:2,name:'Soft structure shirt',type:'Clothing',price:138,color:'Pale blue',tag:'AUREFASH edit',image:'photo-1598554747436-c9293d6a588f',alt:'Modern tailored shirt'},
 {id:3,name:'Sculpted shoulder bag',type:'Accessories',price:196,color:'Cocoa',tag:'Bestseller',image:'photo-1584917865442-de89df76afd3',alt:'Sculptural leather shoulder bag'},
 {id:4,name:'The Sunday knit',type:'Clothing',price:164,color:'Ivory',tag:'New in',image:'photo-1576566588028-4147f3842f27',alt:'Soft textured knitwear'},
 {id:5,name:'Everywhere sunglasses',type:'Accessories',price:112,color:'Tortoise',tag:'Small batch',image:'photo-1511499767150-a48a237f0083',alt:'Classic tortoiseshell sunglasses'},
 {id:6,name:'The column dress',type:'Clothing',price:218,color:'Black',tag:'AUREFASH edit',image:'photo-1539008835657-9e8e9680c956',alt:'Minimal black occasion dress'},
 {id:7,name:'Studio leather belt',type:'Accessories',price:94,color:'Espresso',tag:'Just in',image:'product-belt.svg',alt:'Espresso leather belt with a brushed gold buckle'},
 {id:8,name:'Easy day trouser',type:'Clothing',price:172,color:'Stone',tag:'Bestseller',image:'photo-1509631179647-0177331693ae',alt:'Relaxed neutral tailoring'}
];
const photo=(id,w=900)=>id.endsWith('.svg')?`assets/${id}`:`https://images.unsplash.com/${id}?auto=format&fit=crop&w=${w}&q=82`;
const money=n=>'$'+n.toFixed(0);
const state={cart:JSON.parse(localStorage.getItem('af-cart')||'[]').map(x=>typeof x==='number'?{id:x,size:''}:x),filter:'All'};
const card=p=>`<article class="product-card"><button class="product-image" data-product="${p.id}" aria-label="View ${p.name}"><img src="${photo(p.image)}" alt="${p.alt}" loading="lazy"><span class="product-tag">${p.tag}</span><span class="quick-view">Quick view <img src="assets/icon-arrow.svg" alt=""></span></button><div class="product-meta"><div><p>${p.name}</p><span>${p.color} · ${p.type}</span></div><b>${money(p.price)}</b></div></article>`;
document.querySelector('#new-grid').innerHTML=products.slice(0,4).map(card).join('');
function renderAll(){const items=state.filter==='All'?products:products.filter(p=>p.type===state.filter);document.querySelector('#all-grid').innerHTML=items.map(card).join('');}
renderAll();
document.addEventListener('click',e=>{
 const filter=e.target.closest('[data-filter]');if(filter){state.filter=filter.dataset.filter;document.querySelectorAll('.filter').forEach(x=>x.classList.toggle('active',x===filter));renderAll();}
 const filterLink=e.target.closest('[data-filter-link]');if(filterLink){state.filter=filterLink.dataset.filterLink;document.querySelectorAll('.filter').forEach(x=>x.classList.toggle('active',x.dataset.filter===state.filter));renderAll();}
 const category=e.target.closest('[data-category]');if(category){state.filter=category.dataset.category;document.querySelectorAll('.filter').forEach(x=>x.classList.toggle('active',x.dataset.filter===state.filter));renderAll();}
 const prod=e.target.closest('[data-product]');if(prod)openProduct(+prod.dataset.product);
 if(e.target.closest('[data-cart]'))openCart();
 if(e.target.closest('[data-close]'))closeCart();
 if(e.target.closest('[data-dialog-close]'))document.querySelectorAll('dialog[open]').forEach(d=>d.close());
 const remove=e.target.closest('[data-remove]');if(remove){state.cart=state.cart.filter((_,i)=>i!==+remove.dataset.remove);saveCart();}
 if(e.target.closest('.checkout-button'))document.querySelector('#notice-dialog').showModal();
 if(e.target.closest('[data-menu]'))document.querySelector('.nav-left').classList.toggle('mobile-open');
 if(e.target.closest('[data-search]')){const q=prompt('Search the AUREFASH edit');if(q){state.filter='All';renderAll();const first=products.find(p=>p.name.toLowerCase().includes(q.toLowerCase()));if(first)openProduct(first.id);else toast('No pieces found for “'+q+'”.');}}
});
document.querySelector('#product-detail').addEventListener('click',e=>{const size=e.target.closest('[data-size]');if(size){document.querySelectorAll('[data-size]').forEach(x=>x.classList.toggle('selected',x===size));return;}const b=e.target.closest('[data-add]');if(!b)return;const p=products.find(x=>x.id===+b.dataset.add),selected=document.querySelector('[data-size].selected');if(p.type==='Clothing'&&!selected){toast('Choose a size to continue');return;}state.cart.push({id:p.id,size:selected?.dataset.size||'One size'});saveCart();document.querySelector('#product-dialog').close();toast('Added to your bag');});
function openProduct(id){const p=products.find(x=>x.id===id),sizes=p.type==='Clothing'?['XS','S','M','L']:['One size'];document.querySelector('#product-detail').innerHTML=`<img class="detail-img" src="${photo(p.image,1000)}" alt="${p.alt}"><div class="detail-copy"><p class="eyebrow">${p.type} · ${p.tag}</p><h2>${p.name}</h2><b>${money(p.price)}</b><p>A thoughtful wardrobe piece with a relaxed line, considered details and an easy feel. Made to move through the day with you.</p><label>Colour <strong>${p.color}</strong></label><div class="swatch"><i></i><i></i><i></i></div><label>Size <strong>${p.type==='Clothing'?'Choose a size':'One size'}</strong></label><div class="sizes">${sizes.map(s=>`<button data-size="${s}">${s}</button>`).join('')}</div><button class="button add-button" data-add="${p.id}">Add to bag <img src="assets/icon-arrow-light.svg" alt=""></button><small>Free shipping on orders over $150</small></div>`;document.querySelector('#product-dialog').showModal();}
function openCart(){document.querySelector('.overlay').classList.add('visible');document.querySelector('.cart-drawer').classList.add('open');document.body.classList.add('no-scroll');}
function closeCart(){document.querySelector('.overlay').classList.remove('visible');document.querySelector('.cart-drawer').classList.remove('open');document.body.classList.remove('no-scroll');}
function saveCart(){localStorage.setItem('af-cart',JSON.stringify(state.cart));renderCart();}
function renderCart(){const wrap=document.querySelector('.cart-items'),list=state.cart.map((item,i)=>({p:products.find(p=>p.id===item.id),size:item.size,i}));wrap.innerHTML=list.map(({p,size,i})=>`<div class="cart-item"><img src="${photo(p.image,260)}" alt=""><div><b>${p.name}</b><span>${p.color}${size?` · ${size}`:''}</span><strong>${money(p.price)}</strong><button data-remove="${i}">Remove</button></div></div>`).join('');document.querySelectorAll('.bag-count').forEach(x=>x.textContent=state.cart.length);document.querySelector('.subtotal').textContent=money(list.reduce((s,x)=>s+x.p.price,0));document.querySelector('.cart-empty').style.display=list.length?'none':'block';document.querySelector('.cart-foot').style.display=list.length?'block':'none';}
function toast(msg){const t=document.querySelector('.toast');t.textContent=msg;t.classList.add('show');setTimeout(()=>t.classList.remove('show'),2300);}
document.querySelector('#newsletter-form').addEventListener('submit',e=>{e.preventDefault();document.querySelector('#notice-dialog').showModal();e.target.reset();});
document.addEventListener('keydown',e=>{if(e.key==='Escape'){closeCart();document.querySelector('.nav-left').classList.remove('mobile-open');}});
renderCart();
